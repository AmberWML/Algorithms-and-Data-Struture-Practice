#Ruohan wang
#wang8039

import traceback

#huffman_encode: Takes in a single String input_string, which is
# the string to be encoded.  Computes the optimal binary encoding
# of the string and encodes it, returning a String of 0s and 1s.
# This is not an actual Python binary string, just a normal String
# that happens to contain only 0s and 1s.
def huffman_encode(input_string):
    lib = {}
    for ch in input_string:
        if ch in lib:
            lib[ch] += 1
        else:
            lib[ch] = 1
    minq = []
    for ch in lib:
        newNode = node(ch,lib[ch])
        min_heap_insert(minq,newNode)
    for i in range(len(lib)-1):
        low = heap_extract_min(minq)
        low2 = heap_extract_min(minq)
        super_ch = low.ch + low2.ch
        super_freq = low.freq + low2.freq
        super_node = node(super_ch, super_freq)
        super_node.left = low
        super_node.right = low2
        min_heap_insert(minq, super_node)
    root = heap_extract_min(minq)
    result = ''
    
    def Encode(ch,root):
        code = ''
        node = root
        ch = input_string[i]
        while ch != node.ch:
            if ch in (node.left.ch):
                node = node.left
                code = code + '0'
            elif ch in (node.right.ch):
                node = node.right
                code = code + '1'
        return code
    
    for i in range(len(input_string)):
        result = result + Encode (input_string[i],root)
    return result

    


class node:
    def __init__(self,ch,freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None
    def __repr__(self):
        return self.ch+":"+str(self.freq)



def min_heapify(Q,i):
    l = 2*i+1
    r = 2*i+2
    smallest = i
    if l < len(Q) and Q[l].freq < Q[smallest].freq:
        smallest = l
    if r < len(Q) and Q[r].freq < Q[smallest].freq:
        smallest = r
    if i != smallest:
        Q[i],Q[smallest] = Q[smallest],Q[i]
        min_heapify(Q,smallest)
        
    
def heap_extract_min(Q):
    if len(Q) == 1:
        return Q.pop()
    minElement = Q[0]
    Q[0] = Q.pop()
    min_heapify(Q,0)
    return minElement

def parent(i):
    return int((i-1)/2)

def min_heap_insert(Q,node):
    Q.append(node)
    i = len(Q) - 1
    while i > 0 and Q[parent(i)].freq > Q[i].freq:
        Q[parent(i)],Q[i] = Q[i],Q[parent(i)]
        i = parent(i)



    


#  DO NOT EDIT BELOW THIS LINE

tests = ['message0.txt','message1.txt','message2.txt','message3.txt',
         'message4.txt','message5.txt']
correct = ['message0encoded.txt','message1encoded.txt',
           'message2encoded.txt','message3encoded.txt',
           'message4encoded.txt','message5encoded.txt']


#Run test cases, check whether encoding correct
count = 0

try:
    for i in range(len(tests)):
        ("\n---------------------------------------\n")
        print("TEST #",i+1)
        print("Reading message from:",tests[i])
        fp = open(tests[i])
        message = fp.read()
        fp.close()
        print("Reading encoded message from:",correct[i])
        fp2 = open(correct[i])
        encoded = fp2.read()
        fp2.close()
        output = huffman_encode(message)
        if i < 5:
            print("Running: huffman_encode on '"+message+"'\n")
            print("Expected:",encoded,"\nGot     :",output)
        assert encoded == output, "Encoding incorrect!"
        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)
except Exception:
    print("\nFAIL: ",traceback.format_exc())


print(count,"out of",len(tests),"tests passed.")


