# Project Description (Caching-Algorithm)
In this project, you will design a caching algorithm for your users to improve user experience by reducing delay and also to save bandwidth for your organization. In this scenario, there are 100 files with varying popularity and sizes. Users request these files based on their popularity.

You have a limited cache space where you can store some of the files after they have been requested by a user. Hence, you can satisfy some of the user requests from the cache and save bandwidth of your organization. Your aim is to maximize the amount of data that is satisfied from the cache, hence minimize the consumed bandwidth which we refer to as the hit_penalty in the code.

There might also be a cost associated with replacing files in the cache. As writing and removing files from the disk might be costly, you might also want to reduce the amount data replaced in the cache. This parameter is called as replacement_penalty which you can assume 0 for parts 1 and 2.

The popularity of the files are distributed geometrically where the most popular files are much more popular than the least popular files, hence, you will find that some files are very frequently requested. The sizes of the files are also geometrically distributed. Hence, some files may fill up your cache very quickly. There is no correlation between the size and popularity of a file.

# Part 1
In this part, a simpler version of the problem is given to you. Your caching algorithm has access to information about file popularity and size. Try to find an algorithm which will minimize the hit_penalty.

# Part 2
In this part, you will not have access to file popularity and file size information beforehand. If you need that information, you have to infer that information keeping track of user requests. This is a much challenging problem.

For this part, I expect you to look into the literature to get inspiration. A useful keyword might be “multi-armed bandits”. I do not expect a complete literature review but you will get a higher grade by tying your ideas to the literature and properly citing them. It is also possible that you refer to other sources such as blog posts but make sure to write in your own words and cite your sources.

# Part 3
In this part, you will increase the cost of replacement to 0.1. This will mean you need to keep the cache more stable not to increase the replacement cost.
