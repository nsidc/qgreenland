// We can't reproduce the issue we're seeing with the "real" config in this
// simple example...
#some_struct: {
  args: [...string]
}
#Template: {
  _foo: string
  ...
  bar: [...#some_struct]
}


#some_template: #Template & {
  _foo: string
  _bar: string

  bar: [
    #some_struct & {
      args: [
        "foo",
        "bar",
        _foo,
        _bar,
      ]
    },
  ]
}


things: {
  thing_a: #templates.some_template & {
    _foo: "baz"
    _bar: "banana"
  }
}
#templates: {
  some_template: #some_template
}
