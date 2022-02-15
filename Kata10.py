def main():
    try:
        open("config.txt")
    except:
        print('No se encontró el archivo config.txt')
if __name__ == '__main__':
    main()