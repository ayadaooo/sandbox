Console.WriteLine("Hello, World!");

int age = 21;
string name = "Adrian";
double gpa = 4.0;
bool isFulltime = true;

double price = 19.99;

Console.WriteLine("Name: " + name);
Console.WriteLine("Age: " + age);
Console.WriteLine("GPA: " + gpa);
Console.WriteLine("Full-time student: " + isFulltime);


if (age >= 18)
{
    Console.WriteLine(name + " is an adult.");
}
else
{
    Console.WriteLine(name + " is a minor.");
}

int count = 0;
while (count < 5) ;
{
    Console.WriteLine("Count: " + count);
    count++;
}

for (int i = 0; i < 5; i++)
{
    Console.WriteLine(i);
}

int input;
do
{
    Console.WriteLine("Enter a number greater than 0:");
    input = int.Parse(Console.ReadLine());
}
while (input <= 0);

switch (grade)
{
    case "A":
        Console.WriteLine("Excellent");
        break;
    case "B":
        Console.WriteLine("Good");
        break;
    default:
        Console.WriteLine("Unknown");
        break;
}


max = (num1 > num2) ? num1 : num2;

if (num1 > num2)
{
    max = num1;
}
else
{
    max = num2;
}

int x = 4;
Console.WriteLine(x++); // prints 4
Console.WriteLine(++x); // prints 6

static int Add(int a, int b)
{
    return a + b;
}

static void DisplayBanner()
{
    Console.WriteLine("Welcome");
}

int total = Add(5, 3);
Console.WriteLine(total);

static void Increment(int num)
{
    num++;
}

int value = 10;
Increment(value);
Console.WriteLine(value); // still prints 10, not 11

static int Increment(int num)
{
    return num + 1;
}

int value = 10;
value = Increment(value); // reassigning value to the result
Console.WriteLine(value); // now prints 11

