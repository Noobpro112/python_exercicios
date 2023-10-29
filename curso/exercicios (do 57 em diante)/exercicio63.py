quantos=int(input("Quantos numeros da sequencia de fibonacci você quer ver? "))
fn=0
f1=1
while quantos > 0:
    fn=f1+fn
    print(fn)
    f2=fn
    fn=f1
    f1=f2
    quantos-=1
