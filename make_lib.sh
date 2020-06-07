rm -Rf lib.zip
cd venv/lib/python3.8/site-packages
zip -r9 ${OLDPWD}/lib.zip .
cd ${OLDPWD}