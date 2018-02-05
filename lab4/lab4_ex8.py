import sys
import os
import binascii
import shutil

#WORKS BUT NOT PERFECTLY... I HAVE AN ERROR

# 8. Sa se scrie un script care primeste urmatoarele argumente: path, tree_depth, filesize , filecount, dircount si care
# creeaza o structura de directoare de adancime depth astfel: incepand din radacina path vor fi create dircount directoare
# si filecount fisiere cu continut de filesize octeti (doar caracterul "a" de exemplu") iar acest proces va fi repetat
# recursiv pentru fiecare director creat pana cand se obtine adancimea dorita (in directoarele aflate la adacimea maxima
# nu se vor crea alte directoare)
#
# De exemplu, daca rulam scriptul astfel: python3 create_dummy_tree.py test 2 1024 3 3 va fi creat in directorul curent
# urmatoarea structura:
#
#     test
#     test/dir0
#     test/dir0/file1 (size 1024)
#     test/dir0/file2 (size 1024)
#     test/dir0/file3 (size 1024)
#
#     test/dir1
#     test/dir1/file1 (size 1024)
#     test/dir1/file2 (size 1024)
#     test/dir1/file3 (size 1024)
#
#     test/dir2
#     test/dir2/file1 (size 1024)
#     test/dir2/file2 (size 1024)
#     test/dir2/file3 (size 1024)
#
#     test/file0 (size 1024)
#     test/file1 (size 1024)
#     test/file2 (size 1024)



def exercitiul_8():
    if len(sys.argv) < 6 :
        print("Few arguments... expected 5 arguments, received ", len(sys.argv) - 1)
    else:
        path = sys.argv[1]
        global tree_depth
        tree_depth = int(sys.argv[2])
        filesize = int(sys.argv[3])
        filecount = int(sys.argv[4])
        dircount = int(sys.argv[5])

        def create_files(path):
            os.chdir(path)
            count = filecount - 1
            while count >= 0:
                name = "file" + str(count) + ".txt"
                f = open(name, "wb+")
                f.seek(filesize-1)
                f.write(binascii.a2b_uu(b'a'))
                f.close()
                count -= 1

        def create_directories(path):
            os.chdir(path)
            count = dircount - 1
            while count >= 0:
                name = "dir" + str(count)
                os.mkdir(name)
                count -= 1

        def recursive_function(tree_depth, path):
            while(tree_depth > 0 ):
                os.chdir(path)
                create_directories(path)
                tree_depth -= 1
                for (root, directories, files) in os.walk(path):
                    for dirName in directories:
                        path2 = os.path.join(path, dirName)
                        create_files(path2)
                        recursive_function(tree_depth, path2)

        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))

            create_files(path)
            recursive_function(tree_depth, path)
        else:
            print("Entered path it doesn't exist... Please enter a valid path...")
            print(path)
print("\nRaspuns exercitiul 8:")
exercitiul_8()

# Arguments: "F:\PyCharm Workspace\PyhtonLabs\lab4\recursiveTree" 2 1024 3 3