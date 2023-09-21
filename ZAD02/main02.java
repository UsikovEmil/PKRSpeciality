package ZAD02;
import java.util.PriorityQueue;

public class main02 {
    private String id;
    private String name;
    private int frequency;

    public main02(String id, String name, int frequency) {
        this.id = id;
        this.name = name;
        this.frequency = frequency;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getFrequency() {
        return frequency;
    }

    public static void main(String[] args) {
        main02 toy1 = new main02("1", "Медведь", 5);
        main02 toy2 = new main02("2", "Кукла", 3);
        main02 toy3 = new main02("3", "Лего", 7);

        PriorityQueue<main02> toys = new PriorityQueue<>((a, b) -> b.getFrequency() - a.getFrequency());
        toys.add(toy1);
        toys.add(toy2);
        toys.add(toy3);

        while (!toys.isEmpty()) {
            System.out.println(toys.poll().getName());
        }
    }
}
