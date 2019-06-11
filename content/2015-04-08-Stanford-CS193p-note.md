Title: Note for Stanford CS193p
Date: 2015-04-08
Category: Studying

### Class 2
What's the different between exclamation mark and question mark after the vars?
they are same, but exclamation mark means the var will automatical unwrap.

```
@IBOutlet weak var display: UILabel!
@IBOutlet weak var display: UILabel?
```

### Class 3
Same way to instance array and dictionary

```
var opStack = Array<Op>()
var opStack = [Op]()

var knowOps = Dictionary<String, Op>()
var knowOps = [String:Op]()
```

In Swift Array and Dictionary is struct, not class. When passed to argument, they are copied.
Copied isn't copy actually, untill the value has be changed.

### Class 4
lazy

only var can lazy initialized, let can't.

init method

There is a free init for class and struct

Designated init:

 initialize all properties introduced by you class, before calling a superclass's init (different with Obj-C and C++) 
 Convenience init:
 Must call designated init

AnyObject

cast with <font color="blue">as </font>

check with <font color="blue">is</font>

```
var b: AnyObject
var a = b as? UIButton 

if b is UIButton {

}
```

String.Index

Unicode characters, can use Int to index a string

### Class 5

The two method to hierarchy in code

```
addSubview(aView: UIView) // sent to a aVies's superview
removeFromSuperView()    // this is send to the view you want to remove
```



<p>{{ page.date | date_to_string }}</p>