./bin/build.sh

while inotifywait --event modify --format '%w' ./sections/*.md
do
  ./bin/build.sh
done
