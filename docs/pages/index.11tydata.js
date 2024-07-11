const fs = require('fs')
const path = require('path')

const schemaFiles = fs.readdirSync('schemas/').filter(file => path.extname(file) === '.json')

module.exports = function () {
  return {
    CI_PROJECT_NAME: process.env.CI_PROJECT_NAME,
    schemaFiles
  }
}
