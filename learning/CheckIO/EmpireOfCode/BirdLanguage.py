# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Package 
# Version 


VOWELS = "aeiouy"


def translate(phrase):
    """
    Bird Language

    Robots keep little mechbirds as pets. Recently, they were trying to teach it how to speak basic language.
    Today the bird spoke its first word: "hieeelalaooo". This sounds a lot like "hello", but with too many
    vowels. With the information they discovered, we should help them to make a translation module.

    The bird converts words by two rules:

    - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
    - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
    Vowels letters == "aeiouy".

    You are given an ornithological phrase as several words which are separated by white-spaces (each pair of
    words by one whitespace). The bird does not know how to punctuate its phrases and only speaks words as
    letters. All words are given in lowercase. You should translate this phrase from the bird language to
    something more understandable.

    :param phrase: A bird phrase as a string.
    :return: The translation as a string.
    """

    for word in phrase.strip().split():
        pass



    return phrase


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

