from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

keydict = {'q':0,'2':1,'w':2,'e':3,'4':4,'r':5,'5':6,'t':7,'y':8,'7':9,'u':10,'8':11,'i':12,'9':13,'o':14,'p':15,'-':16,'[':17,'=':18,']':19}

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    strings = []
    for i in range(20):
        strings.append(GuitarString(440*(1.059463**(i-12))))

    pluckedstrings = set()
    sample = 0

    n_iters = 0
    while True:
        # it turns out that the bottleneck is in polling for key events
        # for every iteration, so we'll do it less often, say every 
        # 1000 or so iterations
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        # check if the user has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            key_index = keydict.get(key, -1)
            if key_index != -1: 
                strings[key_index].pluck()
                pluckedstrings.add(strings[key_index])

        # compute the superposition of samples
        if len(pluckedstrings) != 0:
            sample = sum(x.sample() for x in pluckedstrings)

        # play the sample on standard audio
        play_sample(sample)

        # advance the simulation of each guitar string by one step
        for x in pluckedstrings.copy():
            x.tick()
            if x.time() > 220500:
                pluckedstrings.remove(x)

