import { StyleSheet, View, FlatList } from "react-native";

import { RepositoryCardSkeleton } from "./components/repository-card.skeleton";

export function PageGithubSkeleton() {
  return (
    <View style={styles.container}>
      <View style={styles.conatainerUserInformation}>
        <View style={styles.containerImage} />
        <View style={styles.name} />
      </View>
      <FlatList
        style={styles.list}
        data={Array(6).fill(null)}
        keyExtractor={(_, index) => index.toString()}
        renderItem={() => <RepositoryCardSkeleton />}
      />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    paddingTop: 32,
    alignItems: "center"
  },
  conatainerUserInformation: {
    justifyContent: "center",
    alignItems: "center",
    gap: 8
  },
  containerImage: {
    width: 150,
    height: 150,
    backgroundColor: "#777",
    borderRadius: 50
  },
  name: {
    backgroundColor: "#777",
    width: 150,
    height: 30,
  },
  list: {
    marginTop: 16,
    flex: 1,
    gap: 2,
  }
});
