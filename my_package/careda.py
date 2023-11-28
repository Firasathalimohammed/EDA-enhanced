class ClassDistribution:
    def __init__(self, data):
        self.data = data

    def plot_distribution(self):
        class_counts = self.data['class'].value_counts()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=class_counts.index, y=class_counts.values)
        plt.title('Distribution of Class Labels')
        plt.xlabel('Classification')
        plt.ylabel('Count')
        plt.show()


class PriceMaintenanceRelation:
    def __init__(self, data):
        self.data = data

    def plot_price_maintenance_relation(self, price_col, maint_col, class_col):
        plt.figure(figsize=(12, 6))

        # Price vs Classification
        plt.subplot(1, 2, 1)
        sns.countplot(x=price_col, hue=class_col, data=self.data)
        plt.title('Buying Price vs Classification')
        plt.xlabel('Buying Price')
        plt.ylabel('Count')

        # Maintenance Cost vs Classification
        plt.subplot(1, 2, 2)
        sns.countplot(x=maint_col, hue=class_col, data=self.data)
        plt.title('Maintenance Cost vs Classification')
        plt.xlabel('Maintenance Cost')
        plt.ylabel('Count')

        plt.tight_layout()
        plt.show()



class SafetyAnalysis:
    def __init__(self, data):
        self.data = data

    def plot_safety_relation(self, safety_col, class_col):
        plt.figure(figsize=(10, 6))
        sns.countplot(x=safety_col, hue=class_col, data=self.data)
        plt.title('Safety Rating vs Classification')
        plt.xlabel('Safety Rating')
        plt.ylabel('Count')
        plt.show()



class CapacityAnalysis:
    def __init__(self, data):
        self.data = data

    def plot_capacity_relation(self, doors_col, persons_col, class_col):
        plt.figure(figsize=(12, 6))

        # Number of Doors vs Classification
        plt.subplot(1, 2, 1)
        sns.countplot(x=doors_col, hue=class_col, data=self.data)
        plt.title('Number of Doors vs Classification')
        plt.xlabel('Number of Doors')
        plt.ylabel('Count')

        # Passenger Capacity vs Classification
        plt.subplot(1, 2, 2)
        sns.countplot(x=persons_col, hue=class_col, data=self.data)
        plt.title('Passenger Capacity vs Classification')
        plt.xlabel('Passenger Capacity')
        plt.ylabel('Count')

        plt.tight_layout()
        plt.show()



class LuggageBootSizeAnalysis:
    def __init__(self, data):
        self.data = data

    def plot_luggage_boot_relation(self, boot_size_col, class_col):
        plt.figure(figsize=(10, 6))
        sns.countplot(x=boot_size_col, hue=class_col, data=self.data)
        plt.title('Luggage Boot Size vs Classification')
        plt.xlabel('Luggage Boot Size')
        plt.ylabel('Count')
        plt.show()
