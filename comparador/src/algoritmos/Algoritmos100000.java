import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.Random;

public class Algoritmos100000 {
public static void randomnumber(int[] a) {
        Random rand = new Random();
        for (int i = 0; i < a.length; i++) {
            a[i] = rand.nextInt(100) + 1;
        }
    }

    public static void printarray(int[] a) {
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
        
        System.out.println();
    }

    // ========== ALGORITMOS DE ORDENAMIENTO ==========
    
    // 1. Selection Sort
    public static int[] selectionSort(int[] a) {
        for (int i = 0; i < a.length; i++) {
            int small = i;
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] < a[small]) {
                    small = j;
                }
            }
            int temp = a[small];
            a[small] = a[i];
            a[i] = temp;
        }
        return a;
    }
    
    // 2. Bubble Sort
    public static int[] bubbleSort(int[] a) {
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a.length - i - 1; j++) {
                if (a[j] > a[j + 1]) {
                    int temp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = temp;
                }
            }
        }
        return a;
    }
    
    // 3. Insertion Sort
    public static int[] insertionSort(int[] a) {
        for (int i = 1; i < a.length; i++) {
            int temp = a[i];
            int j = i - 1;
            while (j >= 0 && temp < a[j]) {
                a[j + 1] = a[j];
                j = j - 1;
            }
            a[j + 1] = temp;
        }
        return a;
    }
    
    // 4. Quick Sort
    public static int[] quickSort(int[] a) {
        quickSort(a, 0, a.length - 1);
        return a;
    }
    
    private static void quickSort(int[] a, int low, int high) {
        if (low < high) {
            int pi = partition(a, low, high);
            quickSort(a, low, pi - 1);
            quickSort(a, pi + 1, high);
        }
    }
    
    private static int partition(int[] a, int low, int high) {
        int pivot = a[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (a[j] <= pivot) {
                i++;
                swap(a, i, j);
            }
        }
        swap(a, i + 1, high);
        return i + 1;
    }
    
    private static void swap(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
    
    // 5. Merge Sort
    public static int[] mergeSort(int[] a) {
        mergeSort(a, 0, a.length - 1);
        return a;
    }
    
    private static void mergeSort(int[] a, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            mergeSort(a, left, mid);
            mergeSort(a, mid + 1, right);
            merge(a, left, mid, right);
        }
    }
    
    private static void merge(int[] a, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        for (int i = 0; i < n1; i++)
            L[i] = a[left + i];
        for (int j = 0; j < n2; j++)
            R[j] = a[mid + 1 + j];

        int i = 0, j = 0, k = left;

        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                a[k] = L[i];
                i++;
            } else {
                a[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            a[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            a[k] = R[j];
            j++;
            k++;
        }
    }
    
    // 6. Heap Sort
    public static int[] heapSort(int[] a) {
        int n = a.length;

        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(a, n, i);

        for (int i = n - 1; i > 0; i--) {
            swap(a, 0, i);
            heapify(a, i, 0);
        }
        return a;
    }
    
    private static void heapify(int[] a, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && a[left] > a[largest])
            largest = left;

        if (right < n && a[right] > a[largest])
            largest = right;

        if (largest != i) {
            swap(a, i, largest);
            heapify(a, n, largest);
        }
    }
    
    private static int[] hacerSemiOrdenado(int[] arr) {
        int n = arr.length;
        int[] semiOrdenado = arr.clone();
        
        // Intercambiamos algunos elementos aleatorios para crear un arreglo semi-ordenado
        Random rand = new Random();
        int numIntercambios = n / 10; // Intercambiar aproximadamente el 10% de los elementos
        
        for (int i = 0; i < numIntercambios; i++) {
            int idx1 = rand.nextInt(n);
            int idx2 = rand.nextInt(n);
            swap(semiOrdenado, idx1, idx2);
        }
        
        return semiOrdenado;
    }
    
    public static int[] heapSortSemiOrdenado(int[] a) {
        int n = a.length;
        
        // Primero ordenamos completamente el arreglo
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(a, n, i);

        for (int i = n - 1; i > 0; i--) {
            swap(a, 0, i);
            heapify(a, i, 0);
        }
        
        // Luego lo desordenamos parcialmente (semi-ordenado)
        return hacerSemiOrdenado(a);
    }
    
    public static int[] heapSortInverso(int[] a) {
        int n = a.length;

        // Ordenamos en orden inverso usando un min-heap en lugar de max-heap
        for (int i = n / 2 - 1; i >= 0; i--)
            heapifyInverso(a, n, i);

        for (int i = n - 1; i > 0; i--) {
            swap(a, 0, i);
            heapifyInverso(a, i, 0);
        }
        return a;
    }

    // Versión de heapify para orden inverso (min-heap)
    private static void heapifyInverso(int[] a, int n, int i) {
        int smallest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && a[left] < a[smallest])
            smallest = left;

        if (right < n && a[right] < a[smallest])
            smallest = right;

        if (smallest != i) {
            swap(a, i, smallest);
            heapifyInverso(a, n, smallest);
        }
    }
    
    // 7. Shell Sort
    public static int[] shellSort(int[] a) {
        int n = a.length;
        int gap = n / 2;
        while (gap > 0) {
            for (int i = gap; i < n; i++) {
                int temp = a[i];
                int j = i;
                while (j >= gap && a[j - gap] > temp) {
                    a[j] = a[j - gap];
                    j -= gap;
                }
                a[j] = temp;
            }
            gap /= 2;
        }
        return a;
    }
    
    // 8. Counting Sort (para Radix Sort)
    private static void countingSortForRadix(int[] a, int exp) {
        int n = a.length;
        int[] output = new int[n];
        int[] count = new int[10];

        for (int i = 0; i < n; i++) {
            int index = (a[i] / exp) % 10;
            count[index]++;
        }

        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }

        for (int i = n - 1; i >= 0; i--) {
            int index = (a[i] / exp) % 10;
            output[count[index] - 1] = a[i];
            count[index]--;
        }

        System.arraycopy(output, 0, a, 0, n);
    }
    
    // 9. Radix Sort
    public static int[] radixSort(int[] a) {
        int max = Arrays.stream(a).max().getAsInt();

        int exp = 1;
        while (max / exp > 0) {
            countingSortForRadix(a, exp);
            exp *= 10;
        }
        return a;
    }
    
    // 10. Bucket Sort
    public static int[] bucketSort(int[] inputArr) {
        int s = inputArr.length;
        ArrayList<ArrayList<Integer>> bucketArr = new ArrayList<>();
        for (int i = 0; i < s; i++) {
            bucketArr.add(new ArrayList<>());
        }

        int maxVal = Arrays.stream(inputArr).max().getAsInt();

        for (int j : inputArr) {
            double normalized = (double) j / (maxVal + 1);
            int bi = (int) (s * normalized);
            bucketArr.get(bi).add(j);
        }

        for (ArrayList<Integer> bucket : bucketArr) {
            int[] bucketArray = bucket.stream().mapToInt(i -> i).toArray();
            insertionSort(bucketArray);
            for (int i = 0; i < bucket.size(); i++) {
                bucket.set(i, bucketArray[i]);
            }
        }

        int idx = 0;
        for (ArrayList<Integer> bucket : bucketArr) {
            for (int j : bucket) {
                inputArr[idx++] = j;
            }
        }
        return inputArr;
    }
    
    
    
    public static java.util.Map<String, Double> ejecutarAlgoritmo() {
        java.util.Map<String, Double> tiempos = new java.util.HashMap<>();
        int[] arrayOriginal = new int[100000];
        randomnumber(arrayOriginal);
        
        System.out.println("=== EJECUTANDO CON 100 ELEMENTOS ===");
        System.out.println("Arreglo Original (primeros 10): ");
        printarray(arrayOriginal);
        System.out.println("Arreglo Ordenado");
        printarray(heapSort(arrayOriginal));
        System.out.println("Arreglo Semi-Ordenado");
        printarray(heapSortSemiOrdenado(arrayOriginal));
        System.out.println("Arreglo Inverso");
        printarray(heapSortInverso(arrayOriginal));
        
        // Medir tiempo para cada algoritmo
        tiempos.put("Selection Sort", medirTiempo(arrayOriginal, "selection"));
        tiempos.put("Bubble Sort", medirTiempo(arrayOriginal, "bubble"));
        tiempos.put("Insertion Sort", medirTiempo(arrayOriginal, "insertion"));
        tiempos.put("Quick Sort", medirTiempo(arrayOriginal, "quick"));
        tiempos.put("Merge Sort", medirTiempo(arrayOriginal, "merge"));
        tiempos.put("Heap Sort", medirTiempo(arrayOriginal, "heap"));
        tiempos.put("Shell Sort", medirTiempo(arrayOriginal, "shell"));
        tiempos.put("Radix Sort", medirTiempo(arrayOriginal, "radix"));
        tiempos.put("Bucket Sort", medirTiempo(arrayOriginal, "bucket"));
        
        System.out.println("\n=== RESULTADOS ===");
        for (Map.Entry<String, Double> entry : tiempos.entrySet()) {
            System.out.printf("%s: %.4f ms\n", entry.getKey(), entry.getValue());
        }
        
        return tiempos;
    }
    
    private static double medirTiempo(int[] arrayOriginal, String algoritmo) {
        int[] copia = arrayOriginal.clone();
        long inicio = System.nanoTime();
        
        switch(algoritmo) {
            case "selection": selectionSort(copia); break;
            case "bubble": bubbleSort(copia); break;
            case "insertion": insertionSort(copia); break;
            case "quick": quickSort(copia); break;
            case "merge": mergeSort(copia); break;
            case "heap": heapSort(copia); break;
            case "shell": shellSort(copia); break;
            case "radix": radixSort(copia); break;
            case "bucket": bucketSort(copia); break;
        }
        
        long fin = System.nanoTime();
        double tiempo = (fin - inicio) / 1_000_000.0;
        
        // Verificar que está ordenado
        if (!estaOrdenado(copia)) {
            System.out.println("⚠️  " + algoritmo + " no ordenó correctamente");
        }
        
        return tiempo;
    }
    
    private static boolean estaOrdenado(int[] a) {
        for (int i = 0; i < a.length - 1; i++) {
            if (a[i] > a[i + 1]) return false;
        }
        return true;
    }
    
    // Método main para pruebas
    public static void main(String[] args) {
        ejecutarAlgoritmo();
    }
}
