def main():
    try:
        open("config.txt")
    except:
        print('No se encontrĂ³ el archivo config.txt')
if __name__ == '__main__':
    main()