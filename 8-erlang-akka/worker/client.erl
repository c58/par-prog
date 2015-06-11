#!/usr/bin/env escript
%%! -sname w@worker -setcookie secret

-module(client).

client() ->
  receive
    start ->
      {server, s@dispatcher} ! {self(), listing},
      client();

    {listing, FilesList} ->
      FileName = lists:nth(2, FilesList),
      {server, s@dispatcher} ! {self(), content, FileName},
      client();

    {content, Content} ->
      io:fwrite(Content)
  end.

main(_) ->
  net_kernel:connect_node(s@dispatcher),
  self() ! start,
  client().