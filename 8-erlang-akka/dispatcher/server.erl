#!/usr/bin/env escript
%%! -sname s@dispatcher -setcookie secret

-module(server).

server() ->
  receive
    {From, listing} ->
      {ok, Cwd} = file:get_cwd(),
      FilesList = filelib:wildcard(Cwd ++ "/*"),
      From ! {listing, FilesList},
      server();

    {From, content, FileName} ->
      {ok, Binary} = file:read_file(FileName),
      Lines = string:tokens(erlang:binary_to_list(Binary), "\n"),
      From ! {content, Lines},
      server()
  end.

main(_) ->
  Pid = spawn(fun() -> server() end),
  register(server, Pid),
  receive _ -> ok end.