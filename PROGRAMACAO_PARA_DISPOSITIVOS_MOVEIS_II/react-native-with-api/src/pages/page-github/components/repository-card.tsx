import { StyleSheet, Text, View } from "react-native";
import { generateNewColor, pickTextColorBasedOnBgColorAdvanced } from "../../../utils/generate-color";
import { memo } from "../../../utils/memo";

type RepositoryCardProps = {
  name: string;
  description: string | null;
  language: string | null;
}

const colorTag: Record<string, string> = {
  "JavaScript": "#FAE94B",
  "Python": "#00A816",
  "TypeScript": "#1563D6",
  "Kotlin": "#D68929",
  "Elixir": "#7610E3",
  "PHP": "#CF54E6"
}

const getColorTag = memo((language: string | null) => (language && colorTag[language]) ?? generateNewColor());

export function RepositoryCard({ name, description, language }: RepositoryCardProps) {
  const colorRGB = getColorTag(language);
  const fontColor = pickTextColorBasedOnBgColorAdvanced(colorRGB, "#FFF", "#000");

  return (
    <View style={styles.container}>
      <Text style={styles.name}>{name}</Text>
      {description && <Text style={styles.description}>{description}</Text>}
      {language && (
        <View style={styles.containerTag}>
          <View style={{ ...styles.tag, backgroundColor: colorRGB, }}>
            <Text style={{
              backgroundColor: colorRGB,
              color: fontColor
            }}>
              {language}
            </Text>
          </View>
        </View>
      )}
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    display: "flex",
    marginTop: 12,
    marginBottom: 12,
    borderColor: "#ccc",
    borderTopWidth: 1,
    paddingTop: 12,
    alignItems: "center"
  },
  name: {
    fontSize: 20,
    fontWeight: "bold",
    color: "#fff",
    textAlign: "center"
  },
  description: {
    fontSize: 12,
    color: "#fff",
    textAlign: "justify"
  },
  containerTag: {
    justifyContent: "center",
    alignItems: "center"
  },
  tag: {
    marginTop: 8,
    padding: 8
  },
  textTag: {
    fontSize: 10,
  },
});
