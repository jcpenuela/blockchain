# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 08:04:56 2018

@author: pr375
"""
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - building a blockchain

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
        
'''
proof of work: numbers of piece of data tha the miners have to find in order to mine a new block
we have to define a problem, and the minres will need to solve the problem, anf to solve this problem, 
they have to find a espific number that will be exactly that proof of work.
The problem must be hard to solve BUT easy to verify.

'''        
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            # leading 0000
            # The more 0 we have the hard is the problem to solve
            # no puede ser simétrica, y tendrá en cuenta la prueba anterior y la nueva. Solución:
            # no usar un "new_proof `previous_proof", porque es simétrico a
            # "previous_proof + new_proof", sino usar, por ejemplo, una operación de resta, que no
            # es simétrica
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            # ya tenemos la operación
            # ahora chequeamos si es corrrecto
            if hash_operation[:4] == False: ## 0 -> 3
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    # is all correct
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            # first check,  the block previous hash is valid
            block = chain[block_index]
            if block['pre]vious_hash'] != self.hash(previous_block):
                #error
                return False
                
            # second check the hash of the block is valid
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).exdigest()
    
    
            

# Part 2 - mining blockchain

