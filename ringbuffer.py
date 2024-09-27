#!/usr/bin/env python3

class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''
        # TO-DO: implement this
        self.MAX_CAP = capacity
        self._front = 0
        self._rear = 0
        self.buffer = []
        self._size = 0
        for n in range(self.MAX_CAP):
            self.buffer.append(None)

    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''
        return self._size
    
    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        return self.size() == 0
        
    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        return self.size() == self.MAX_CAP

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        if self.is_full():
            raise RingBufferFull("Buffer is full")
        else:
            self.buffer[self._rear] = x
            self._rear += 1
            if self._rear == self.MAX_CAP:
                self._rear = 0
            self._size += 1


    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        if self.is_empty():
            raise RingBufferEmpty("Buffer is empty")
        else:
            x = self.buffer[self._front]
            self.buffer[self._front] = None
            self._front += 1
            if self._front == self.MAX_CAP:
                self._front = 0
            self._size -= 1
        return x

    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        if self.is_empty():
            raise RingBufferEmpty("Buffer is empty")
        else:
            return self.buffer[self._front]


class RingBufferFull(Exception):
    '''
    The exception raised when the ring buffer is full when attempting to
    enqueue.
    '''
    pass

class RingBufferEmpty(Exception):
    '''
    The exception raised when the ring buffer is empty when attempting to
    dequeue or peek.
    '''
    pass
