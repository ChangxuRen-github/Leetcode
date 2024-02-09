[Java-8-streams](https://www.baeldung.com/java-8-streams)
Overview
========
Requires basic knowledge of Java 8 (lambda expression, Optional, method references).


Stream Creation
===============
There are many ways to create a stream instance of different sources. 
Once created, the instance will not modify its source, therefore allowing the creation of multiple instances from a single source.

Empty Stream
============
We should use the empty() method in case of the creation of an empty stream: 
```Java
Stream<String> streamEmpty = Stream.empty();
```

We often use the empty() method upon creation to avoid returning null for streams with no elemnts.

Stream of Collection
====================
We can create a stream of any type of Collection(Collection, List, Set)
```Java
Collection<String> collection = Arrays.asList("a", "b", "1");
Stream<String> streamOfCollection = collection.stream();
```

Stream of Array
===============
An array can also be the source of a stream:
```Java
Stream<String> streamOfArray = Stream.of("1", "2", "3");
String[] arr = new String[]{"1", "2", "3"};
Stream<String> streamOfArrayFull = Arrays.stream(arr);
Stream<String> streamOfArrayPart = Arrays.stream(arr, 1, 3);
```


Stream.builder()
================
When builder is used, the desired type should be additionally specified in the right part of the statement, 
otherwise the build() method will create an instance of the Stream<Object>.
```Java
Stream<String> streamBuilder = Stream.<String>builder().add("a").add("b").add("c").build();
```


Stream.generate()
=================
The generate() method accepts a Supplier<T> for element generation. As the resulting stream is infinite, 
the developer should specify the desired size, or the generate() method will work until it reaches the memory limit.
```Java
Stream<String> streamGenerated = Stream.generate(()->"element").limit(10);
// The code above creates a sequence of ten strings with the value "element"
```


Stream.iterate()
================
Another way of creating an infinite stream is by using the iterate() method:
```Java
Stream<Integer> streamIterated = Stream.iterate(40, n->n+2).limit(20);
```
The first element of the resulting stream is the first parameter of the iterate() method. 
When creating every following element, the specified function is applied to the previous element. In the example
above the second element will be 42.


Stream of Primitives
====================
Java 8 offers the possibility to create streams out of three primitive types: int, long and double.
As stream<T> is a generic interface, and there is no way to use primitives as a type parameter with generics, 
three new special interfaces were created: IntStream, LongStream, DoubleStream.


Using the new interfaces alleviates unnecessary auto-boxing, which allows for increased productivity:
```Java
IntStream intStream = IntStream.range(1, 3);
LongStream longStream = LongStream.rangeClosed(1, 3);
```
The range(int startInclusive, int endExclusive) method create an ordered stream from the first parameter to the second 
parameter. It increments the value of subsequent elements with the step equal to 1. The result does not include the last
parameter, it is just an upper bound of the sequence.

The rangeClosed(int startInclusive, int endInclusive) method does the same thing with only one difference, the second element
is included. We can use these two methods to generate any of the three types of streams of primitive. 


Stream of String
================
We can also use String as a source for creating a stream with the help of the chars() method of the String class.
Since there is no interface for CharStream in JDK, we use the IntStream to represent a stream oif chars instead.
```Java
IntStream streamOfChars = "abc".chars();
```
The following example breaks a String into sub-strings according to specified RegEx.
```Java
Stream<String> streamOfString = Pattern.compile(", ").splitAsStream("a, b, c");
```



