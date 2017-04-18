from mpi4py import MPI
import array

sendbuf = array.array('d', [0]*10)
recvbuf = array.array('d', [0]*10)
tag = 0
status = MPI.Status()

myrank = MPI.COMM_WORLD.Get_rank()

if myrank == 0:
    sendbuf[0]=10;
    sendbuf[1]=11;
    print("rank 0 before sendbuf[0],sendbuf[1],recvbuf[0],recvbuf[1]", sendbuf[0],sendbuf[1],recvbuf[0],recvbuf[1])
    MPI.COMM_WORLD.Send([sendbuf, MPI.DOUBLE], 1, tag)
    print("rank 0 after sendbuf[0],sendbuf[1],recvbuf[0],recvbuf[1]", sendbuf[0],sendbuf[1],recvbuf[0],recvbuf[1])
elif myrank == 1:
    print("rank 1 before recvbuf[0],recvbuf[1]", recvbuf[0],recvbuf[1] )
    MPI.COMM_WORLD.Recv([recvbuf, MPI.DOUBLE], 0, tag, status)
    print("rank 1 after recvbuf[0],recvbuf[1]", recvbuf[0],recvbuf[1] )