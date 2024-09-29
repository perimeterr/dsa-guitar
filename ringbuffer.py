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
        self.buffer = [None] * capacity

    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''
        if self._rear > self._front:
            return self._rear - self._front
        elif self._rear < self._front:
            return self.MAX_CAP - self._front + self._rear + 1
        else:
            return 0 if self.buffer[self._rear] == None else self.MAX_CAP
    
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
        self.buffer[self._rear] = x
        self._rear += 1
        if self._rear == self.MAX_CAP: self._rear = 0

    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        if self.is_empty():
            raise RingBufferEmpty("Buffer is empty")
        x = self.buffer[self._front]
        self.buffer[self._front] = None
        self._front += 1
        if self._front == self.MAX_CAP: self._front = 0
        return x

    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        if self.is_empty():
            raise RingBufferEmpty("Buffer is empty")
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
