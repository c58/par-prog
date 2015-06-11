namespace py ranker

service Ranker {
  list<string> getNodesByUrl (1: string url)
}