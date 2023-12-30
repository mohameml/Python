# La condition  **`if __name__ == "__main__":`**


La ligne de code **`if __name__ == "__main__":`** est une condition couramment utilisée dans les scripts Python. 

Son rôle principal est de déterminer si le fichier Python est exécuté en tant que script principal ou s'il est importé comme module dans un autre script.

Lorsqu'un fichier Python est exécuté en tant que script principal, c'est-à-dire directement à partir de la ligne de commande ou d'un environnement de développement intégré (IDE), la variable **`__name__`** est automatiquement définie à la valeur spéciale **`"__main__"`**. En revanche, si le fichier est importé en tant que module, la variable **`__name__`** est définie avec le nom réel du module.

La condition **`if __name__ == "__main__":`** permet donc d'identifier si le fichier est exécuté en tant que script principal. Ce bloc de code qui suit cette condition est exécuté uniquement lorsque le fichier est exécuté directement. Cela permet d'avoir un code spécifique qui sera exécuté lorsque le fichier est lancé en tant que script, mais pas lorsque le fichier est importé comme module.

L'utilisation la plus courante de cette condition est d'inclure des instructions de test ou des exemples d'utilisation dans le bloc de code qui suit. Ainsi, lorsque le fichier est exécuté directement, ces instructions de test seront exécutées. Cependant, si le fichier est importé comme module, ces instructions ne seront pas exécutées automatiquement.

En résumé, la condition **`if __name__ == "__main__":`** est utilisée pour déterminer si le fichier Python est exécuté en tant que script principal. Cela permet d'avoir du code spécifique qui ne sera exécuté que lorsque le fichier est lancé directement, et pas lorsqu'il est importé comme module.