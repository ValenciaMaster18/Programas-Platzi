def main():
    nombres = {"Luis","Luna","Luis","Luis","Luz"}

    nombres.add("Miguel") 
    nombres.update([1,2,3])
    
    nombres.remove(1)
    nombres.discard(3)
    nombres.pop()
    nombres.clear()
    
    return print(nombres)
    

if __name__ == "__main__":
    main()