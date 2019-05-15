import { rename } from "fs"

// @ts-check

const fs = require("fs")

let files = fs.readdirSync("./")
files = files.filter(isSectionFile).map(extractNumbers)
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

// function rename(files, depth, prefix) {
//   let i = 0
//   for (const file of files) {
//     if (isSectionFile(file)) {
//       const name = extractNumbers(file)
//       const newName = `${i}.${name.name}`
//       fs.renameSync(name.full, newName)
//     } else {
//       console.log(file)
//     }
//     i++
//   }

// }

// rename(files, 1, '')
let tree = []

// files.forEach(file => {
//   setPath(tree, file.numbers, file)
// })

for (const key in tree) {
}
setPath(tree, [0], { name: "0" })
setPath(tree, [0, 1], { name: "01" })
setPath(tree, [2, 1], { name: "21" })
setPath(tree, [2], { name: "2" })
console.log(JSON.stringify(tree, null, "  "))

function setPath(obj, path, val) {
  let current = obj
  delete val.numbers
  for (const idx in path) {
    const part = path[idx]
    if (idx === String(path.length - 1)) {
      if (part in current) {
        current[part] = { ...current[part], ...val }
      } else {
        current.push(val)
      }
    } else {
      if (!(part in current)) {
        current[part] = { children: [] }
      }
      if (!("children" in current[part])) {
        current[part].children = []
      }
      current = current[part].children
    }
  }
}
// console.log(files)
