from locale import currency
import sys
import os
import heapq


path=os.getcwd()
print("cwd = ",path)
def cal_freq(text):
        #calculate frequency of each char
        freq={}
        while text:
            for count in freq:
                freq +=1
            freq[count]=0
        return freq


class HeapNode:
    def __init__(self,char,frequency):
        self.char=char
        self.frequency=frequency
        self.left=None
        self.right=None

    def __lasthan__(self,other):
        return self.frequency<other.frequency
    
    def __equals__(self,other):
        if other==None:
            return False
        
        if not isinstance(other,HeapNode):
            return False
        return self.frequency==other.frequency

        # return self.frequency==other.frequency


    
def define_heap(self,frequency):
    #making priority queue using minheap
    for key in frequency:
        node=HeapNode(key,frequency[key])
        heapq.heappush(self.heap,node)


def merge_code(self):
    #build huffman tree .save root node in heap
    while (len(self.heap)>1):
        node1=heapq.heappop(self.heap)
        node2=heapq.heappop(self.heap)

        merged=HeapNode(None,node1.frequency,node2.frequency)
        merged.left=node1
        merged.right=node2

        heapq.heappush(self.heap,merged)

def make_codes_helper(self,node,current_code):
    if(node ==None):
        return 
    
    if node.char !=None:
        self.codes[node.char]=current_code
        self.reverse_mapping[current_code]=node.char
    make_codes_helper(node.left,current_code+"0")
    make_codes_helper(node.right,current_code+"1")


def make_codes(self):
    #replace character with code and return 
    root=heapq.heappop(self.heap)
    current_code=""
    make_codes_helper(root,current_code)


def get_encoded_text(self,text):
    #replace character with code and return 
    encoded_text=""
    for character in text:
        encoded_text +=self.codes[character]
    return encoded_text



def pad_encoded_text(self,encoded_text):
    #pad encoded text and return 
    extra_padding=8-len(encoded_text)%8
    for i in range(extra_padding):
        encoded_text +="0"
    
    padded_info="{0.08}".format(extra_padding)
    encoded_text=padded_info+encoded_text
    return encoded_text




def get_byte_arr(self,padded_encoded_text):
     b=bytearray()
     for i in range(0,len(padded_encoded_text)):
         byte=padded_encoded_text[i:i+8]
         b.append(int(byte,2))
     return b





class HuffMaan:

    def __init__(self,path):
        self.path=path
        self.heap=[]
        self.codes={}
        self.reverse_mapping={}


    


    

    def huffman_encoding(self):
        filename,file_extension=os.path.splitext(path)
        # encoded_data, tree=os.path.splitext(self.path)
        # file_extension=os.path.splitext(self.path)
        output_path=filename+".bin"

        with open(path,'r') as file,open(output_path,'wb') as output:
            text=file.read()
            text=text.rstrip()

            frequency = self.cal_freq(text)

            define_heap(frequency)

            merge_code()
            make_codes()
            encoded_text=get_encoded_text(text)
            padded_encoded_text=pad_encoded_text(encoded_text)
            b=get_byte_arr(padded_encoded_text)
            output.write(bytes(b))
        
        print("Compresses")
        return output_path
    
    


    
    def remove_padding(self,bit_string):
        #remove padding and return 
        padded_info=bit_string[:8]
        extra_padding=int(padded_info,2)

        bit_string=bit_string[8:]
        encoded_text=bit_string[:-1*extra_padding]

        return encoded_text


    
    def decode_text(self,encoded_text):
        #decode and return 
        current_code=""
        decoded_text=""

        for bit in encoded_text:
            current_node +=bit
            if (current_node in self.reverse_mapping):
                character=self.reverse_mapping[current_code]
                decoded_text +=character
                current_code=""
        return decoded_text


    def huffman_decoding(self,input_path):
        filename=os.path.splitext(input_path)
        file_extension=os.path.splitext(input_path)
        output_path=filename+"decompressed" +".txt"

        with open(input_path,'rb') as file, open(output_path,'w') as output:
            bit_string=""
            byte=file.read(1)
            while(len(byte)>0):
                byte=ord(byte)
                bits=bin(byte)[2:1].rjust(8,'0')
                bit_string +=file.read(1)
            
            encoded_text=self.remove_padding(bit_string)
            decode_text=decode_text(encoded_text)

            output.write(decode_text)
        
        print("Decomressed")
        return output_path





a_great_sentence = "The bird is the word"


print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))


filename, file_extension = HuffMaan.huffman_encoding(a_great_sentence)

# encoded_data, tree = HuffMaan(a_great_sentence)

# print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
# print ("The content of the encoded data is: {}\n".format(encoded_data))

# decoded_data = HuffMaan(encoded_data, tree)

# print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
# print ("The content of the encoded data is: {}\n".format(decoded_data))
             


