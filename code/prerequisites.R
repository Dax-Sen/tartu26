htmlwidgets::saveWidget(
  flowmap_seville_interactive,
  file = "docs/seville_flowmap_embed.html",
  selfcontained = TRUE
)
# Upload to gh release
system("gh release upload v1 docs/seville_flowmap_embed.html --repo tdscience/tartu26 --clobber")
