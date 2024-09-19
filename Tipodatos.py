print("Clase v2 Daniel Villar")
# zona de clase
class datos:
    # el constructor funcion multiplos
    def __init__(self, estatura,peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
            print(f"estatura: {self.estatura} mts, peso {self.peso}kg")
    
    def mi_lista(self):
        TopMis3Pokemones=["Espeon","Mimikyu","Piplup"]
        print(TopMis3Pokemones)
        
        for pokemones in TopMis3Pokemones:
            print(pokemones)
        
    #tuplas
    def mi_tupla(self):
        Top3pokemonesFeos=("Hypno","Zubat","whismur")
        print(Top3pokemonesFeos)
        
        for FeosPokemones in Top3pokemonesFeos:
            print(FeosPokemones)
            
    #conjuntos
    def conjunto(self):
        Top3BestMlp=("Fluttershy","Rarity","Luna")
        print(Top3BestMlp)
        
        for Mlp in Top3BestMlp:
            print(Mlp)
    #diccionario
    def Diccionario(self):
        Top3MonsterHighs= {
    "Top 1:": "Twilight", 
    "Top 2:": "Cleo de nile",
    "Top 3:": "Abby"
    }
        print(Top3MonsterHighs)
        for a,e in Top3MonsterHighs.items():
            print(a,e)
            
# creacion de objeto info
info=datos(1.75,80.5)

# utilizando el obj -->▼
info.mostrar_datos()
print("Lista de Mis Top 3 pokemones Daniel Villar")
info.mi_lista()
print("Tuplas de mi Top 3 pokemones Feos Daniel Villar")
info.mi_tupla()
print("Conjunto  de mi Top 3 Personajes Mlp")
info.conjunto()
print("Diccionario de mi Top 3 Personajes Monster high")
info.Diccionario()