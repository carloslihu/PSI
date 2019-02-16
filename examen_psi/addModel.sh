#!/bin/bash

FILE=$1

if [ $FILE -z ]
then
	echo "especifica el fichero pls:"
	read FILE
fi

echo -e "\n" >> $FILE
echo "from django.template.defaultfilters import slugify" >> $FILE
echo "from django.utils.timezone import now" >> $FILE

echo "creating a new model!"

echo "nombre de la clase del modelo:"
read modelClass
echo "class $modelClass(models.Model):" >> $FILE

echo -e "\t#declaracion de tus campos" >> $FILE

echo -e "\tclass Meta:" >> $FILE
echo -e "\t\tpass" >> $FILE
echo -e "\t\t#your code goes here" >> $FILE
echo -e "\tdef __str__(self):" >> $FILE
echo -e "\t\tpass" >> $FILE
echo -e "\t\t#your code goes here" >> $FILE
echo -e "\tdef __unicode__(self):" >> $FILE
echo -e "\t\treturn self.__str__()" >> $FILE
echo -e "\tdef save(self, *args, **kwargs):" >> $FILE
echo -e "\t\t#your code goes here" >> $FILE
echo -e "\t\tsuper($modelClass, self).save(*args, **kwargs)" >> $FILE
echo "" >> $FILE