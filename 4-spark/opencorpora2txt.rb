#!/usr/bin/env ruby
# encoding: utf-8

# The MIT License (MIT)
#
# Copyright (c) 2013-2014 Dmitry Ustalov
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

require 'rubygems'
require 'nokogiri'
require 'unicode_utils/downcase'
require 'csv'

Dir.mkdir 'opencorpora' unless File.directory? 'opencorpora'

buf, flag = '', false
parents, children, names = [], {}, {}

File.foreach('annot.opcorpora.xml') do |s|
  s.tap(&:chomp!).tap(&:strip!)

  next unless flag ||= s =~ /<text.*>/
  buf << s

  unless flag &&= s !~ /<\/text.*>/
    doc = Nokogiri::XML(buf)

    id = doc.xpath('//text/@id').text.to_i
    parent = doc.xpath('//text/@parent').text.to_i
    paragraphs = doc.xpath('//text/paragraphs/paragraph')
    names[id] = doc.xpath('//text/@name').text

    if parent.zero?
      parents << id
    else
      children[id] = parent
    end

    unless paragraphs.empty?
      File.open('opencorpora/%04d.txt' % id, 'w') do |f|
        paragraphs.each do |paragraph|
          tokens = paragraph
            .xpath('sentence/tokens/token')
            .select {|t| t.xpath('tfr/v[1]/l/g[@v="NOUN" or @v="ADJF"]').first}
          f.puts tokens.map {|t| UnicodeUtils.downcase(t["text"])}.join(' ')
        end
      end
    end

    puts 'text #%04d is done' % id
    buf.clear
  end
end

CSV.open('opencorpora/index.csv', 'w') do |csv|
  csv << %w(id parent_id parent_name name)
  children.each do |id, parent_id|
    parent_id = children[parent_id] until parents.include? parent_id
    csv << [id, parent_id, names[parent_id], names[id]]
  end
end