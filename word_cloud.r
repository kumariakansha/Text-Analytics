iris
# Load
library("tm")
library("SnowballC")
library("wordcloud")
library("RColorBrewer")
fileName <- 'C:/Users/akank/Desktop/trump_corrpus.txt'
 text <- readChar(fileName, file.info(fileName)$size)


docs <- Corpus(VectorSource(text))
inspect(docs)
toSpace <- content_transformer(function (x , pattern ) gsub(pattern, " ", x))
docs <- tm_map(docs, toSpace, "/")
docs <- tm_map(docs, toSpace, "@")
docs <- tm_map(docs, toSpace, "\\|")
# Convert the text to lower case
docs <- tm_map(docs, content_transformer(tolower))
# Remove numbers
docs <- tm_map(docs, removeNumbers)
# Remove english common stopwords
docs <- tm_map(docs, removeWords, stopwords("english"))
# Remove your own stop word
# specify your stopwords as a character vector
docs <- tm_map(docs, removeWords, c("himself", "choices")) 
# Remove punctuations
docs <- tm_map(docs, removePunctuation)
# Eliminate extra white spaces
docs <- tm_map(docs, stripWhitespace)
# Text stemming
# docs <- tm_map(docs, stemDocument)
dtm <- TermDocumentMatrix(docs)
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
head(d, 10)
set.seed(1234)
abc <- data.frame(d$word,d$freq)
write.csv(abc,"C:/Users/akank/Desktop/result.csv")
wordcloud(words = d$word, freq = d$freq, min.freq = 1,max.words=200, random.order=FALSE, rot.per=0.35,colors=brewer.pal(8, "Dark2"))
frequency <- read.csv("C:/Users/akank/Desktop/idf.csv")

wordcloud(words = frequency$words, freq = frequency$freq,colors=brewer.pal(6,"Dark2"),scale=c(2,.5),random.order=FALSE,min.freq = 1)