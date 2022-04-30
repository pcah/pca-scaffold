OLD=$1
NEW=$2
git push origin refs/tags/$OLD:refs/tags/$NEW :refs/tags/$OLD && git tag -d $OLD
