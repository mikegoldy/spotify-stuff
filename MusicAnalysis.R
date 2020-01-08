spotify_data <- read.csv("~/Documents/Python projects/Spotify/playlistInfo.csv")

#What makes music loud?

#is loudness & danceability correlated? Ans: Yes
model0 <- lm(loudness ~ danceability, data=spotify_data)
summary(model0)
#is loudness & energy correlated?
model1 <- lm(loudness ~ energy, data=spotify_data)
summary(model1)
#does energy and danceability effect loudness?
model2 <- lm(loudness ~ danceability+energy, data=spotify_data)
summary(model2)
model3 <- lm(spotify_data$loudness ~ spotify_data$danceability*spotify_data$energy)
summary(model3)
#is speechiness & danceability correlated?
model4 <- lm(speechiness ~ danceability, data=spotify_data)
summary(model4)
#is speechiness & energy correlated?
model5 <- lm(speechiness ~ energy, data=spotify_data)
summary(model5)

#rewrite key pitchclass digit to actual key
spotify_data$key[spotify_data$key == 0] <- "C"
spotify_data$key[spotify_data$key == 1] <- "C#"
spotify_data$key[spotify_data$key == 2] <- "D"
spotify_data$key[spotify_data$key == 3] <- "D#"
spotify_data$key[spotify_data$key == 4] <- "E"
spotify_data$key[spotify_data$key == 5] <- "F"
spotify_data$key[spotify_data$key == 6] <- "F#"
spotify_data$key[spotify_data$key == 7] <- "G"
spotify_data$key[spotify_data$key == 8] <- "G#"
spotify_data$key[spotify_data$key == 9] <- "A"
spotify_data$key[spotify_data$key == 10] <- "A#"
spotify_data$key[spotify_data$key == 11] <- "B"

#What makes music positive?

#is popularity & valence correlated?
model6 <- lm(valence ~ popularity, data=spotify_data)
summary(model6)

model7 <- lm(valence ~ loudness, data=spotify_data)
summary(model7)

#is key and valence correlated?
model8 <- lm(valence ~ factor(key) + instrumentalness + energy + danceability +  popularity + loudness, data=spotify_data)
summary(model8)
#does danceability & energy affect valence?
model9 <- lm(valence ~ danceability + energy, data=spotify_data)
summary(model9)
#do different artists have different valences?
model10 <- lm(valence ~ factor(artist), data=spotify_data)
summary(model10)
plot(spotify_data$popularity, spotify_data$valence)

#What makes music popular?

model11 <- lm(popularity ~ instrumentalness, data=spotify_data)
summary(model11)

model11 <- lm(popularity ~ factor(key), data=spotify_data)
summary(model11)

