#!/bin/python3

N = int(input())

trie = {}


def add_word(trie, word):
    # Base case
    if word == "": return

    # TODO: default dict
    if word[0] in trie:
        trie[word[0]]['count'] += 1
    else:
        trie[word[0]] = {'count': 1}
    add_word(trie[word[0]], word[1:])


def find_word(trie, word):
    if word[0] not in trie:
        return 0
    else:
        # Base case
        if len(word) == 1:
            return trie[word[0]]['count']
        else:
            return find_word(trie[word[0]], word[1:])


for i in range(N):
    line = input()
    command, word = line.split()
    if command == "add":
        add_word(trie, word)
    elif command == "find":
        print(find_word(trie, word))
    else:
        print("hop")
