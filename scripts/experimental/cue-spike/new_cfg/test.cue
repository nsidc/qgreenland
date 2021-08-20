#ChildThingA: #ChildThing & {
  attr_a: string
}
#ChildThingB: #ChildThing & {
  attr_b: string
}
#ChildThing: [Id=_]: {
  id: Id
  ...
}

things: [Id=_]: {
  id: Id
  children: #ChildThing
}

things: {
  thing_a: {
    children: {
      child_a: #ChildThingA & {
        attr_a: "foo"
      },
      // child_b: #ChildThingB & {
      //   attr_b: "bar"
      // },
    },
  },
  // thing_b: {
  //   children: {
  //     another_child: #ChildThingA & {
  //       attr_a: "banana"
  //     },
  //     so_many_childs: #ChildThingA & {
  //       attr_b: "wow"
  //     },
  //   },
  // },
}
