# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:42:44 2021

@author: efemuratucarli
"""
# Using encoder and encrypt as models, implement
# the functions decoder and decrypt. Use them to decrypt the message
# 22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*1
# 37*59*11*23*11*1*57*6*173*7*11
# which was encrypted using the opening of Don Quixote.

book = "In a village of La Mancha, the name of which I have \
no desire to call to mind, there lived not long since one of \
those gentlemen that keep a lance in the lance-rack, an old buckler, \
a lean hack, and a greyhound for coursing."

encrypted_message ="22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*\
137*59*11*23*11*1*57*6*173*7*11"

gen_decode_keys = lambda book, encrypted_message : {int(c) : book[int(c)] for c in encrypted_message.split("*") }
decode_keys = gen_decode_keys(book, encrypted_message)
decoder = lambda decode_keys, encrypted_message : "".join([decode_keys[int(c)]for c in encrypted_message.split("*")])
decrypt = lambda book, encrypted_message : decoder(gen_decode_keys(book, encrypted_message),encrypted_message)
decrypt(book,encrypted_message) # it will return the string 'comprehension is incomprehensible'