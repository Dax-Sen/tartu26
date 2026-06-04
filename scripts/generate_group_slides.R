# scripts/generate_group_slides.R
# This script copies slides-template.qmd to group1.qmd ... group4.qmd,
# updating the title to match the group number.

template_file <- "slides-template.qmd"
template_content <- readLines(template_file)

for (i in 1:4) {
  group_file <- paste0("group", i, ".qmd")
  group_title <- paste0("Group ", i, " presentation")
  
  # Replace the title line in the YAML header
  group_content <- gsub('title: "Group Template Presentation"', paste0('title: "', group_title, '"'), template_content)
  
  writeLines(group_content, group_file)
  message("Generated: ", group_file)
}
