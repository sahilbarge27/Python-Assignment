def main():
    filename = input("Enter file name : ")
    try :
          f = open(filename,"r")
          data = f.read()
          print(data)
          f.close
    except:
          print("File Name not found")

if __name__ =="__main__":
        main()
