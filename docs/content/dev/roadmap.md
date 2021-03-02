# Roadmap

This is the planned development roadmap for `plausible`.
 
These features have been chosen to support an example use-case in the [TARG group](http://www.bristol.ac.uk/psychology/research/brain/targ/), after which we hope to recruit more test users to help us continue to chart our roadmap. 
These features are numbered such that "1" is highest priority, etc.

This roadmap is subject to change, but it's provided to give insight into what the developers are thinking, and where we intend the code to go.

## TARG priorities
Get the following features working in R for use with `glm` and `tidyverse` packages:

1. __Defining variables:__  Particularly, dichotomising continuous variables, and choosing a cutoff. 
2. __Missing values:__ Complete case versus discard incomplete.
3. __Choice of covariates:__ Presence/absence of terms in model, given a larger data set.
4. __Exclusions:__ Discarding outliers.
5. __Data Transformations__: E.g. log transformations.