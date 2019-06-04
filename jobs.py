import subprocess 

# for i in range(100):
#     cmd = "bsub -W 00:15 -M 1000 -r -o out.output './one.py --iterations 1 \
#            --project data/project1 --distribution gaussian'"
#     subprocess.run(cmd, shell=True)



# for i in range(100):
#     cmd = "bsub -W 00:15 -M 1000 -r -o out.output './one.py --iterations 1 \
#            --project data/project2 --distribution uniform'"
#     subprocess.run(cmd, shell=True)



for i in range(100):
    cmd = "bsub -W 00:15 -M 1000 -r -o out.output './one.py --iterations 1 \
           --project data/project3 --distribution zipf'"
    subprocess.run(cmd, shell=True)
