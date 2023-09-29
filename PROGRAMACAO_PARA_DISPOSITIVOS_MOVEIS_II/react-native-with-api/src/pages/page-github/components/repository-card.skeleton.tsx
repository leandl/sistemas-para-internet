import { StyleSheet, View } from "react-native";


export function RepositoryCardSkeleton() {
  return (
    <View style={styles.container}>
      <View style={styles.name} />
      <View style={styles.description} />
      <View style={styles.tag} />
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
    minWidth: "100%",
    alignItems: "center",
    justifyContent: "center"
  },
  name: {
    backgroundColor: "#777",
    width: 150,
    height: 30
  },
  description: {
    marginTop: 1,
    backgroundColor: "#777",
    minWidth: "100%",
    height: 80
  },
  tag: {
    marginTop: 8,
    padding: 8,
    backgroundColor: "#777",
    width: 150,
    height: 30
  },
});
