# Используем готовый образ Java
FROM eclipse-temurin:11-jre-focal

# Копируем JAR-файл в контейнер
COPY aqa-shop.jar app.jar

# Запускаем приложение
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]