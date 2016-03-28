using UnityEditor;

public class VCS
{
    public static void Setting()
    {
        EditorSettings.serializationMode = SerializationMode.ForceText;
        EditorSettings.externalVersionControl = "Visible Meta Files";
    }
}
