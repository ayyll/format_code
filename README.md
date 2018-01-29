# Why And What?
It is a code formatting script,and you may confuse that why I don't use like [astyle](https://sourceforge.net/projects/astyle/),this kind of existing script.In fact,**I used it but it didn't work**.So I write a script by pyton to satisfy some special needs of me.

# Power
Now it has the following two functions:
1. replace Tab with **four** spaces
2. change parenthesis style

about the second function,such as:

```
if()
{
	//do something
}
else
{
	//do something
}

for()
{
	//do something
}
```

and we can change to the unix styte:

```
if() {
	//do something
} else {
	//do something
}

for() {
	//do something
}
```

# Use
Put the exe file in your work directory,and run it,this will format the **files with suffix .c .h** in your work directory,just enjoy it~