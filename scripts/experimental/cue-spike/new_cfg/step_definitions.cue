package Steps

#Step: {
  type: string
  ...
}
#CommandStep: #Step & {
  type: "command"
  args: [...string]
}
