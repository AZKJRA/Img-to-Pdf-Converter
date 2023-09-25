import img2pdf
import time
import glob

def start_infos():
    infos = [
        "Logiciel pour convertir des fichiers Images en PDF",
        "Attention !!!!!!!!! Asurez-vous d'avoir executer ce programme dans le meme repertoire que des fichiers a convertir ",
        "Vous Devez Simplement Entrez le Nom et Le Nombres des Fichiers a convertir",
    ]

    for inf in infos:
        print(inf)
        print()
        time.sleep(1.7)


def get_files_numbers():
    return int(input("Entrez le nombres des fichiers a convertir: "))

def get_files_names():
    numbers = get_files_numbers()
    files = []
    found = glob.glob("*")
    if numbers:
        for nbs in range(numbers):
            name = input(f"Entrez le nom pour le fichier {nbs+1}: ")
            for fd in found:
                if fd == name:
                    if name.endswith(".jpg") or name.endswith(".jpeg") or name.endswith(".png"):
                        files.append(name)
                    else:
                        print("Les Fichiers doivent etre de type (jpg) (jpeg) (png) ././././././././.")
                else:
                    print("Desole Fichier Introuvable ......................././././././././././")
    return files


def converter_programme():
    try:
        files = get_files_names()
        if files:
            for fls in files:
                conv = img2pdf.convert(fls)
                conv_file = open(f"{fls}.pdf", "wb")
                conv_file.write(conv)
                conv_file.close()
        else:
            print("Fin du Processus ..............././././././././././././././././.")
    except:
        print("Fin du Processus ..............././././././././././././././././.")


start_infos()

converter_programme()

input()