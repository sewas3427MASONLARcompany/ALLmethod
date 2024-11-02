import random, string
import webbrowser

print(">>> DISCORD NITRO CODE GENERATOR <<< ")
print(">>> by Atlas | Nulled.to <<< \n\n\n ")
webbrowser.open('https://www.nulled.to/user/1229709-atlas')

num=input('Input How Many Codes to Generate: ')

f=open("Nitro Codes.txt","w", encoding='utf-8')

print("Generating...")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write(y)
   f.write("\n")

f.close()
input("\n\nFinished, Press enter to exit. Codes saved in Nitro Codes")
