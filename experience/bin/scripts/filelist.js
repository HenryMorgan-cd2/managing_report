// @ts-check

const fs = require("fs")

let files = fs
  .readdirSync("./sections")
  .filter(isSectionFile)
  .map(extractNumbers)
files.sort((a, b) => {
  return comp(a.numbers[0], b.numbers[0], () => {
    return comp(a.numbers.length, b.numbers.length, () => {
      return comp(a.numbers[1], b.numbers[1], () => 0)
    })
  })
})

files.map(file => file.nameWas).forEach(name => console.log(`sections/${name}`))

// compare the numbers, if the same then call the resolve function
function comp(a, b, resolveEqual) {
  if (a < b) return -1
  if (a > b) return 1
  return resolveEqual()
}
function extractNumbers(file) {
  const parts = file.split(".")
  const sectionName = parts[parts.length - 2]

  const name = `${sectionName}.md`
  const numbers = parts.slice(0, parts.length - 2).map(Number)
  return { numbers, name, nameWas: file }
}

function isSectionFile(file) {
  return file.match(/(\d+\.)+\w+\.md/)
}
