echo "Replace opening double quote and closing double quote and ellipsis" 
sed -i "s/“/\"/g" ./corpus/*
sed -i "s/”/\"/g" ./corpus/*
sed -i "s/…/.../g" ./corpus/*

echo "Done!"