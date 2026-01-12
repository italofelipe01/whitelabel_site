module.exports = {
  "branches": ["master", "main"],
  "plugins": [
    "@semantic-release/commit-analyzer",      // Analisa os commits para decidir a versão (major/minor/patch)
    "@semantic-release/release-notes-generator", // Gera o texto do changelog
    
    // Opcional: Gera o arquivo CHANGELOG.md no repo
    [
      "@semantic-release/changelog",
      {
        "changelogFile": "CHANGELOG.md"
      }
    ],

    // ESTE é o plugin que cria a Release no GitHub (o que você quer)
    "@semantic-release/github", 

    // Opcional: Commita o CHANGELOG.md de volta no repo
    [
      "@semantic-release/git",
      {
        "assets": ["CHANGELOG.md"], // Note que removi o package.json daqui
        "message": "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
      }
    ]
  ]
};